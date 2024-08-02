#NOTE this compleat fpr oop

class DsicordMembers:
    def __init__(self, first_name, last_name, role):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    def display_information(self):
        return self.first_name, self.last_name,  self.role
    
    def set_new_roel(self, new_role):
        self.role = new_role

member1 = DsicordMembers("najjab", "na", "client")

print(member1.first_name)# => najjab
print(member1.last_name)# => na
print(member1.role)# => client

#Getter
print(member1.display_information())# => ('najjab', 'na', 'client')

#Setter
member1.set_new_roel("nopa")
print(member1.display_information())#? => ('najjab', 'na', 'nopa')