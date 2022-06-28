from datetime import datetime
from sqlalchemy.orm import Session
from database import models


class Base:
    def __init__(self, db: Session):
        self.db = db


class Project(Base):

    def get_project(self, project_id):
        db_data = self.db.query(models.Project).filter(models.Project.id == project_id).first()
        return db_data

    def get_projects(self):
        db_data = self.db.query(models.Project).all()
        return db_data

    def create_project(self, project_info):
        data = models.Project(**project_info.dict())
        data.create_user = 'laughing'
        data.create_time = datetime.now()
        data.update_user = ''
        data.update_time = datetime.now()
        self.db.add(data)
        self.db.commit()
        self.db.flush()
        return data

    def update_project(self, prj):
        db_data = self.db.query(models.Project).filter(models.Project.id == prj.id).first()
        db_data.name = prj.name
        db_data.platform = prj.platform
        db_data.updateuser = prj.updateuser
        self.db.commit()
        self.db.flush()
        return prj

    def delete_project(self, prj_id):
        db_project = self.db.query(models.Project).filter(models.Project.id == prj_id)
        db_project.delete()
        self.db.commit()
        self.db.flush()
        return db_project


class User(Base):

    def get_user(self, user_id):
        db_data = self.db.query(models.User).filter(models.User.id == user_id).first()
        return db_data

    def get_user_by_name(self, username):
        db_data = self.db.query(models.User).filter(models.User.username == username).first()
        return db_data

    def get_users(self):
        db_data = self.db.query(models.User).all()
        return db_data

    def create_user(self, prj):
        data = models.User(**prj.dict())
        self.db.add(data)
        self.db.commit()
        self.db.flush()
        return data

    def update_user(self, user):
        db_data = self.db.query(models.User).filter(models.User.id == user.id).first()
        self.db.commit()
        self.db.flush()
        return user


class Element(Base):
    def get_element(self, ele_id):
        ori_data = self.db.query(models.Element).filter(models.Element.id == ele_id).first()
        return ori_data

    def get_element_by_name(self, ele_name):
        ori_data = self.db.query(models.Element).filter(models.Element.name == ele_name).first()
        return ori_data

    def get_elements(self):
        ori_data = self.db.query(models.Element).all()
        return ori_data

    def create_element(self, element):
        db_element = models.Element(**element.dict())
        self.db.add(db_element)
        self.db.commit()
        return db_element

    def update_element(self, element):
        db_element = self.db.query(models.Element).filter(models.Element.id == element.id).first()
        db_element.name = element.name
        db_element.element = element.element
        db_element.locator = element.locator
        db_element.project = element.project
        db_element.updateuser = element.updateuser
        self.db.commit()
        return element

    def delete_element(self, ele_id):
        db_element = self.db.query(models.Element).filter(models.Element.id == ele_id)
        db_element.delete()
        self.db.commit()
        return ele_id


class Step(Base):
    def get_step(self, step_id):
        db_data = self.db.query(models.Step).filter(models.Step.id == step_id).first()
        return db_data

    def get_step_by_name(self, step_name):
        db_data = self.db.query(models.Step).filter(models.Step.name == step_name).first()
        return db_data

    def get_steps(self):
        db_data = self.db.query(models.Step).all()
        return db_data

    def create_step(self, step):
        req_data = models.Step(**step.dict())
        self.db.add(req_data)
        self.db.commit()
        return req_data

    def update_step(self, step):
        db_data = self.db.query(models.Step).filter(models.Step.id == step.id).first()
        db_data.name = step.name
        db_data.project = step.project
        db_data.element = step.element
        db_data.value = step.value
        db_data.option = step.option
        db_data.updateuser = step.updateuser
        self.db.commit()
        return db_data

    def delete_step(self, step_id):
        db_data = self.db.query(models.Step).filter(models.Step.id == step_id)
        db_data.delete()
        self.db.commit()
        return db_data


class Suite(Base):
    def get_suite(self, suite_id):
        db_data = self.db.query(models.Suite).filter(models.Suite.id == suite_id).first()
        return db_data

    def get_suite_by_name(self, suite_name):
        db_data = self.db.query(models.Suite).filter(models.Suite.name == suite_name).first()
        return db_data

    def get_suites(self):
        db_data = self.db.query(models.Suite).all()
        return db_data

    def create_suite(self, suite):
        req_data = models.Suite(**suite.dict())
        self.db.add(req_data)
        self.db.commit()
        return req_data

    def update_suite(self, suite):
        db_data = self.db.query(models.Suite).filter(models.Suite.id == suite.id).first()
        db_data.name = suite.name
        db_data.project = suite.project
        db_data.step = suite.step
        db_data.updateuser = suite.updateuser
        self.db.commit()
        return db_data

    def delete_suite(self, suite_id):
        db_data = self.db.query(models.Suite).filter(models.Suite.id == suite_id)
        db_data.delete()
        self.db.commit()
        return db_data


class Case(Base):
    def get_case(self, case_id):
        db_data = self.db.query(models.Case).filter(models.Case.id == case_id).first()
        return db_data

    def get_cases(self):
        db_data = self.db.query(models.Case).all()
        return db_data

    def create_case(self, case):
        req_data = models.Case(**case.dict())
        self.db.add(req_data)
        self.db.commit()
        return req_data

    def update_case(self, case):
        db_data = self.db.query(models.Case).filter(models.Case.id == case.id).first()
        db_data.name = case.name
        db_data.level = case.level
        db_data.tag = case.tag
        db_data.status = case.status
        db_data.project = case.project
        db_data.content = case.content
        db_data.updateuser = case.updateuser
        self.db.commit()
        return db_data

    def update_case_result(self, case):
        db_data = self.db.query(models.Case).filter(models.Case.id == case.id).first()
        db_data.result = case.result
        self.db.commit()
        return case

    def delete_case(self, case_id):
        db_data = self.db.query(models.Case).filter(models.Case.id == case_id)
        db_data.delete()
        self.db.commit()
        return db_data


class Option(Base):
    def get_options(self):
        db_data = self.db.query(models.Option).all()
        return db_data
