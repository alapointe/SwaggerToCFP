    
class Helpers():

    # TODO Refactor since summary is not the key anymore
    def sort_dict_by_value(data):
        def get_summary(value):
            return value.get("summary", "")

        sorted_values = sorted(data.items(), key=lambda item: get_summary(item[1]))
        return dict(sorted_values)

    def sort_dict_by_keys(input_dict):
        sorted_dict = {k: input_dict[k] for k in sorted(input_dict)}
        return sorted_dict
    
    @staticmethod
    def sort_dict_by_keys_extended(input_obj):
        if isinstance(input_obj, dict):
            # Trier les clés du dictionnaire et appliquer récursivement sur les valeurs
            return {k: Helpers.sort_dict_by_keys_extended(input_obj[k]) for k in sorted(input_obj)}
        
        elif isinstance(input_obj, list):
            # Trier la liste et appliquer récursivement sur chaque élément
            try:
                # Trier en plaçant None en premier, puis les autres éléments
                sorted_list = sorted(input_obj, key=lambda x: (x is None, x))
            except TypeError:
                # Si le tri échoue (types incompatibles), conserver l'ordre original
                sorted_list = input_obj.copy()
            
            return [Helpers.sort_dict_by_keys_extended(element) for element in sorted_list]
        
        else:
            # Retourner l'objet tel quel pour les autres types
            return input_obj