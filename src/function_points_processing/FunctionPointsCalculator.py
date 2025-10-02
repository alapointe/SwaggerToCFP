

from src.basic_definitions.data import DataMovementType


class FunctionPointsCalculator():

    def __init__(self, movement_types) -> None:
        self.movement_types = movement_types
        # print(self.movement_types)

    def calculate_total_per_spec(self,movement_types) -> int:
        cfp = 0
        for fpid, mvt_types in movement_types.items():
            for mvt_type, datagroup_list in mvt_types.items():
                for datagroup in datagroup_list:
                    cfp += 1
        return cfp
    
    def calculate_entry_count(self, fp_id):
        # print(fp_id)
        for movement_type in self.movement_types[fp_id]:
            if movement_type == DataMovementType.ENTRY : return len(self.movement_types[fp_id][movement_type])

    def calculate_read_count(self, fp_id):
        for movement_type in self.movement_types[fp_id]:
            if movement_type == DataMovementType.READ : return len(self.movement_types[fp_id][movement_type])

    def calculate_write_count(self, fp_id):
        for movement_type in self.movement_types[fp_id]:
            if movement_type == DataMovementType.WRITE : return len(self.movement_types[fp_id][movement_type])

    def calculate_exit_count(self, fp_id):
        for movement_type in self.movement_types[fp_id]:
            if movement_type == DataMovementType.EXIT : return len(self.movement_types[fp_id][movement_type])

    def calculate_total_count(self, fp_id):
        cfp = 0
        for movement_type in self.movement_types[fp_id]:
            cfp += len(self.movement_types[fp_id][movement_type])
        return cfp