from typing import List, Any



class BaseSteps:
    def __init__(self, create_obj:List[Any], request_spec: Any = None):
        self.created_obj = create_obj
        self.request_spec = request_spec
