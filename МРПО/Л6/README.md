paragraphs


# Реляционная модель

1. как переводится на английский язык юзкейс леер?
    * уровень вариантов использования или сервесный слой
2. к какому типу разметки относится xml (структурной либо к семантической)??
    * по мнению относится к семантической разметки, но может к структурной относится
3. ядро не зависит от use case layer, подход? Мы стремимся обеспечить ... ...
    * инверсия зависимости

## Базы данных

![img.png](img.png)

* Предметная область - часть реального мира, подлежащая изучению с целью организации управления и, в конечном итоге,
  автоматизации (образование, экономика, законодательство, медицина)
* Объект предметной области - элемент информационной системы, информацию о котором нужно хранить.
* Фактически база данных это модель предметной области.

* требования в целом к данным предъявляются это:
    * Доступность
    * Изменяемость
    * Согласованность
    * Возможность их аналитической обработки.

## Типы структур данных

![img_1.png](img_1.png)

## Типы моделей

1. Классические
    * Сетевые (теоретико-графовые модели)
    * Иерархические (теоретико-графовые модели)
    * реляционные (теоретико-множественная модель)
2. Современные
    * Пост реляционные
    * Многомерные
    * Объектно-ориентированные

## ORM (Object Relational Model)

ORM - это принцип работы с БД, без использования SQL.

## Требования к коду

![img_2.png](img_2.png)

# SQLAlchemy
___
main.py
```python
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://user:password@localhost:5432/dbname', echo=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)

```

___
models.py
```python 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

employee_workstation_association = Table(
    'employee_workstation_association',
    Base.metadata,
    Column('employee_id', ForeignKey('employee.id'), primary_key=True),
    Column('workstation_id', ForeignKey('workstation.id'), primary_key=True)
)

class Employee(Base):
    __tablename__ = 'employee'
    id: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[int] = mapped_column(nullable=False)
    patronymic: Mapped[str] = mapped_column(nullable=False)
    barcode: Mapped[str] = mapped_column(nullable=False)
    
    workstations: Mapped[Set["Workstation"]] = relationship(secondary=employee_workstation_association,
                                                            back_populates="employees")
    
class Workstation(Base):
    __tablename__ = 'workstation'
    id: Mapped[int] = mapped_column(primary_key=True)
    step: Mapped[int] = mapped_column(nullable=False)    
    employees: Mapped[Set["Employee"]] = relationship(secondary=employee_workstation_association,
                                                      back_populates="workstations")
    equipments: Mapped[List["Equipment"]] = relationship(back_populates="workstation")


class Equipment(Base):
    __tablename__ = 'equipment'
    id: Mapped[int] = mapped_column(primary_key=True)
    tool_URI: Mapped[str] = mapped_column(nullable=False)
    equipment_type: Mapped[int] = mapped_column(nullable=False)
    workstation_id: Mapped[int] = mapped_column(ForeignKey('workstation.id'), nullable=False)
```
