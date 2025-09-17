from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Boolean, Text
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Mapped, mapped_column
from datetime import date

# Database setup
Base = declarative_base()
engine = create_engine('sqlite:///pet_clinic.db')
Session = sessionmaker(bind=engine)
session = Session()


class Owners(Base):
    """Owner model representing pet owners"""
    __tablename__ = 'owners'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=True)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    
    # Relationship to pets (one-to-many)
    pets: Mapped[list["Pets"]] = relationship("Pets", back_populates="owner")
    
    


class Pets(Base):
    """Pet model representing pets in the clinic"""
    __tablename__ = 'pets'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    species: Mapped[str] = mapped_column(String(50), nullable=False)  # e.g., "Dog", "Cat", "Bird"
    breed: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('owners.id'), nullable=False)
    
    # Relationships
    owner: Mapped["Owners"] = relationship("Owners", back_populates="pets")
    appointments: Mapped[list["Appointments"]] = relationship("Appointments", back_populates="pet")
    
    


class Vets(Base):
    """Veterinarian model representing clinic veterinarians"""
    __tablename__ = 'vets'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    specialization: Mapped[str] = mapped_column(String(100), nullable=False)  # e.g., "General", "Surgery", "Dermatology"
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    
    # Relationships
    appointments: Mapped[list["Appointments"]] = relationship("Appointments", back_populates="vet", )
    
    


class Appointments(Base):
    """Appointment model representing pet appointments with veterinarians"""
    __tablename__ = 'appointments'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey('pets.id'), nullable=False)
    veterinarian_id: Mapped[int] = mapped_column(Integer, ForeignKey('vets.id'), nullable=False)
    appointment_date: Mapped[date] = mapped_column(Date, nullable=False)
    notes: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="Scheduled", nullable=False)  # "Scheduled", "Completed", "Cancelled"
    
    # Relationships
    pet: Mapped["Pets"] = relationship("Pets", back_populates="appointments")
    vet: Mapped["Vets"] = relationship("Vets", back_populates="appointments")
    




Base.metadata.create_all(engine)

# vet1 = Vets(name="Dr. Dizzy", specialization="Anesthesiologist", email="dylank@clinic.com")
# vet2 = Vets(name="Dr. James Brown", specialization="Surgery", email="james.brown@clinic.com")
# vet3 = Vets(name="Dr. Lisa Garcia", specialization="Dermatology", email="lisa.garcia@clinic.com")
# vet4 = Vets(name="Dr. Emily Wilson", specialization="General", email="emily.wilson@clinic.com")

# session.add_all([vet1,vet2,vet3,vet4])
# session.commit()

pet1 = Pets(id=1,name= 'greg', species= 'chiuhua' , breed= 'rrer', age= 2, owner_id=1)
pet2 = Pets(id=2,name= 'larry', species= 'great dane' , breed= 'sss', age= 3, owner_id=2),
pet3 = Pets(id=3,name= 'jeff', species= 'husky' , breed='polar' , age= 4, owner_id=3)
pet4 = Pets(id=4,name= 'greg', species= 'poodle' , breed= 'german', age= 2, owner_id=4) 


owner1 = Owners(id=1, name='craig', phone='818-332-1111', email= 'greye@gmail.com', password= 'craig123' )
owner2 = Owners(id=2, name='gordon', phone='818-222-1221', email= 'hey@gmail.com', password= 'gordon223' )
owner3 = Owners(id=3, name='michael', phone='323-112-3453', email= 'good@gmail.com', password= 'michael44' )
owner4 = Owners(id=4, name='harry', phone='555-121-4421', email= 'art123@gmail.com', password= 'harry1' )

appointment1 = Appointments(id=1 , pet_id= 1, veterinarian_id= 1, appointment_date = '2023/11/23', notes= 'needs to reschedule', status = 'canceled')
appointment2 = Appointments(id=2 , pet_id= 2, veterinarian_id= 2 , appointment_date =' 2024/12/22', notes= 'needs to come', status = 'scheduled')
appointment3 = Appointments(id=3 , pet_id= 3, veterinarian_id= 3, appointment_date = '2022/10/12', notes= 'finished', status = 'completed')
appointment4 = Appointments(id=4 , pet_id= 4, veterinarian_id= 4, appointment_date = '2025/11/11' , notes= 'finished', status = 'completed')

#session.add_all([owner1 , owner3, owner4])
session.add_all([appointment1, appointment2, appointment3, appointment4])
session.commit()