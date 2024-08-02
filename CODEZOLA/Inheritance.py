from class_DOCTOR import Doctor
from class_FAMILYDOCTOR import FamilyDoctor

doctor1 = Doctor()


doctor1.studied_years()# => i studied 7 years
doctor1.works_where()# => i work in a hospital
doctor1.paid_by_who()# => i get paid by the government

doctor2 = FamilyDoctor()

doctor2.what_specialization()# => i work with families
doctor2.studied_years()# => i studied 7 years
doctor2.works_where()# => i work in a hospital
doctor2.paid_by_who()# => i get paid by people



from class_FAMILYDOCTOR import FamilyDoctor_1

doctor3 = FamilyDoctor_1()

doctor3.studied_years()# => i studied 7 years
doctor3.works_where()# => i work in a hospital
doctor3.paid_by_who()# => i get paid by people

input("run")