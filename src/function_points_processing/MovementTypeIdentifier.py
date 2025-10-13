from src.basic_definitions.data import DataMovementType, ErreurREST
from utils import logger

class MovementTypeIdentifier():


    def get_movement_types(self, entries, reads, writes, exits) -> dict:
        """
            COSMIC Rule #12

            Params:
                - data_model: dict A dictionnary (str)fpdi : (list)datagroups

            Returns:
                - movement_types: dict a dictionnary containing a list of datagroups per movement types per functional process 
                Ex: fpid : { movement_types : [datagroups] }
        """
        result = {}
        for key in entries:
            result[key] = {
                DataMovementType.ENTRY: entries.get(key, {}).get(DataMovementType.ENTRY, []),
                DataMovementType.READ: reads.get(key, {}).get(DataMovementType.READ, []),
                DataMovementType.WRITE: writes.get(key, {}).get(DataMovementType.WRITE, []),
                DataMovementType.EXIT: exits.get(key, {}).get(DataMovementType.EXIT, [])
            }
        return result
    
    def aggregate_movement_types(self, entries, reads, writes, exits):
        """
            COSMIC Rule #12

            Params:
                - data_model: dict A dictionnary (str)fpdi : (list)datagroups

            Returns:
                - movement_types: dict a dictionnary containing a list of datagroups per movement types per functional process 
                Ex: fpid : { movement_types : [datagroups] }
        """
        result = {}
        for key in entries:
            result[key] = {
                DataMovementType.ENTRY: entries.get(key, {}).get(DataMovementType.ENTRY, []),
                DataMovementType.READ: reads.get(key, {}).get(DataMovementType.READ, []),
                DataMovementType.WRITE: writes.get(key, {}).get(DataMovementType.WRITE, []),
                DataMovementType.EXIT: exits.get(key, {}).get(DataMovementType.EXIT, [])
            }
        return result

    def param_in_properties(self, param, data_model):
        def collect_props(definition):
            """Collect all property names from a group definition, including flat and allOf cases."""
            prop_names = set()
            # Cas propriétés classiques
            if isinstance(definition, dict) and 'properties' in definition:
                prop_names.update(definition['properties'].keys())
            # Cas structure flat (no 'properties')
            elif isinstance(definition, dict):
                prop_names.update(definition.keys())
            # Cas héritage allOf
            if isinstance(definition, dict) and 'allOf' in definition:
                for bloc in definition['allOf']:
                    # Bloc héritage avec propriétés
                    if 'properties' in bloc:
                        prop_names.update(bloc['properties'].keys())
            return prop_names

        all_props = set()
        for definition in data_model.values():
            all_props.update(collect_props(definition))

        # Gestion liste de paramètres
        if isinstance(param, list):
            return any(x in all_props for x in param)
        # Gestion chaîne simple
        return param in all_props

    def find_parent_group(self, param, data_model):
        for group_name, definition in data_model.items():
            if isinstance(definition, dict) and 'properties' in definition:
                if param in definition['properties']:
                    return group_name
            elif param in definition:
                return group_name
        return None 
    
    def identify_entries(self, request_body_datagroups, parameters_datagroups, data_model):
        """
            The entries are described in the requestBody and in the parameters.
            When there is no entry, an UNKNOWN trigger is automatically added. (COSMIC Rule #13)
        """
        entries = {}
        for fpid, datagroups in request_body_datagroups.items():
            entries.update({fpid : {DataMovementType.ENTRY : []}})
            if isinstance(datagroups, dict):
                for key, value in datagroups.items():
                    if self.param_in_properties(datagroups[key], data_model):
                        logger.info("Not a dict")
                    entries.update({fpid : {DataMovementType.ENTRY : datagroups[key]}})

        
        for fpid, datagroups in parameters_datagroups.items():
            (entries[fpid][DataMovementType.ENTRY]).extend(datagroups)
        lst = []
        for fpid, value in request_body_datagroups.items():
            if entries[fpid][DataMovementType.ENTRY] == []:
                entries[fpid][DataMovementType.ENTRY] = ['UNKNOWN'] # COSMIC Rule #13, If no entries, there must be a trigger entry
            lst = list(set(entries[fpid][DataMovementType.ENTRY]))
            entries[fpid][DataMovementType.ENTRY] = lst
        return entries 
     
    def identify_reads_v1(self, entries):
        """
            Pattern : In a service API, all entries are always read (v1).
        """
        return self.transform_entries_to_reads(entries)

    def identify_reads(self, parameters_datagroups):
        """
            Pattern : Read data movement are not part of the scope to be measured.
        """
        reads = {}
        for fpid, datagroups in parameters_datagroups.items():
            reads[fpid] = {DataMovementType.READ: []}
        return reads 
    
    def identify_writes(self, parameters_datagroups):
        """
            Pattern : Write data movement are not part of the scope to be measured.
        """
        writes = {}
        for fpid, datagroups in parameters_datagroups.items():
            writes[fpid] = {DataMovementType.WRITE: []}
        return writes

    @staticmethod
    def identify_exits(self, responses_datagroups):
        """
            Basic approach:
            
            The exits are described in the responses
        """
        exits = {}
        for fpid, datagroups in responses_datagroups.items():
            datagroup_list = []
            for datagroup in datagroups:
                if datagroup in ErreurREST.error_types:
                    datagroup = "ErreurREST"
                datagroup_list.append(datagroup) 
            exits.update({fpid : {DataMovementType.EXIT : list( dict.fromkeys(datagroup_list) )}}) # To remove duplicates from list (ex: ErreurREST)
            if isinstance(datagroups, dict):
                for key, value in datagroups.items():
                    exits.update({fpid : {DataMovementType.EXIT : datagroups[key]}})
        return exits

    @staticmethod
    def transform_entries_to_reads(entries):
        reads = {}
        for operation, movements in entries.items():
            # Vérifier si c'est le cas spécial 'Uploads an image.'
            if operation == 'Uploads an image.':
                reads[operation] = movements
            else:
                # Créer une nouvelle entrée avec READ au lieu de ENTRY
                new_movements = {}
                for mov_type, resources in movements.items():
                    if mov_type == DataMovementType.ENTRY:
                        new_movements[DataMovementType.READ] = resources
                    else:
                        new_movements[mov_type] = resources
                reads[operation] = new_movements
        return reads
