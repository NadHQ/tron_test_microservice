from pydantic import BaseModel


class BaseSerializer(BaseModel):

    model_config = {
        "from_attributes" : True
    }