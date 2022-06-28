from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    status: int
    level: int

    class Config:
        orm_mode = True


class EditUser(BaseModel):
    id: int

    class Config:
        orm_mode = True


class Project(BaseModel):
    project_name: str
    icon: str
    description: str
    version: str
    platform: str

    class Config:
        orm_mode = True


class AddProject(Project):
    createuser: str

    class Config:
        orm_mode = True


class EditProject(Project):
    id: int
    name: str
    platform: str
    updateuser: str

    class Config:
        orm_mode = True


class Element(BaseModel):
    name: str
    element: str
    locator: str
    project: str

    class Config:
        orm_mode = True


class AddElement(Element):
    createuser: str

    class Config:
        orm_mode = True


class EditElement(Element):
    id: int
    name: str
    element: str
    locator: str
    project: str
    updateuser: str

    class Config:
        orm_mode = True


class Step(BaseModel):
    name: str
    project: str
    option: str
    element: str
    value: str

    class Config:
        orm_mode = True


class AddStep(Step):
    createuser: str

    class Config:
        orm_mode = True


class EditStep(Step):
    id: int
    updateuser: str

    class Config:
        orm_mode = True


class Suite(BaseModel):
    name: str
    project: str
    step: str

    class Config:
        orm_mode = True


class AddSuite(Suite):
    createuser: str

    class Config:
        orm_mode = True


class EditSuite(Suite):
    id: int
    updateuser: str

    class Config:
        orm_mode = True


class Case(BaseModel):
    name: str
    project: str
    level: str
    tag: str
    status: str
    content: str

    class Config:
        orm_mode = True


class AddCase(Case):
    createuser: str
    result: str = '未执行'

    class Config:
        orm_mode = True


class EditCase(Case):
    id: int
    updateuser: str

    class Config:
        orm_mode = True


class UpdateCase(BaseModel):
    id: int
    result: str

    class Config:
        orm_mode = True


class Option(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
