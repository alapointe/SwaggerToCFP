import logging

logger = logging.getLogger("logger")
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

# fpid_list = []

class Utils():

    
    @staticmethod
    def generate_fpid(path, http_method, http_method_dict) -> str:
        """
            Paths may have an optional short summary and a longer description for documentation purposes. 
            This information is supposed to be relevant to all operations in this path. description can be multi-line and supports Markdown (CommonMark) for rich text representation.

            OpenAPI defines a unique operation as a combination of a path and an HTTP method. This means that two GET or two POST methods for the same path are not allowed

            https://swagger.io/docs/specification/paths-and-operations/
        """
        fpid  = ""
        if 'summary' in http_method_dict:
            fpid = http_method_dict['summary']
            segments = path.split('/')
            last = segments[-1]
            fpid = fpid + http_method + last
            logger.info(fpid + ' fpid set from summary')
        else:
            segments = path.split('/')
            last = segments[-1]
            fpid = http_method + last
            logger.info(fpid + ' fpid set from description')
        # if fpid in fpid_list:
        #     fpid = f"{fpid}1"
        # fpid_list.append(fpid)
        # for el in fpid_list:
        #     print(el)
        return fpid

    def extract_ref(self, data):
        # Parcourt tous les types de contenu (application/json, etc.)
        for content_type, media_type in data.items():
            schema = media_type.get('schema', {})
            
            # Cas 1 : Référence directe dans le schéma
            ref = schema.get('$ref')
            if ref:
                return ref.split('/')[-1]
            
            # Cas 2 : Référence dans les items d'un tableau
            items = schema.get('items', {})
            ref = items.get('$ref')
            if ref:
                return ref.split('/')[-1]
        
        # Aucune référence trouvée → retourne 'UNKNOWN'
        return "UNKNOWN"
