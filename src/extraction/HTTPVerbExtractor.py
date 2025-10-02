import src.extraction.Extractor as ext
from utils.functional_process_id_generator import Utils as fpig

class HTTPVerbExtractor():

    def get_http_verbs(self, extractor) -> dict:
        paths = extractor.get_paths()
        http_verbs = {}

        for path, http_method in paths.items():
            for http_method, http_method_dict in http_method.items():
                fpid = fpig.generate_fpid(path, http_method, http_method_dict)
                http_verbs.update({fpid : {fpid : http_method}})
        return http_verbs
    