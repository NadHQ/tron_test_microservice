from dataclasses import fields


def orm_to_dto(dto_cls, orm_obj):
    dto_data = {f.name: getattr(orm_obj, f.name) for f in fields(dto_cls)}
    return dto_cls(**dto_data)
