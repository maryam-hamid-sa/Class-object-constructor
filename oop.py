# student class define
class student:
    # add constructor
    def __init__(self,name,age,Cgpa,uni):
        # add attributes
        self.name=name
        self.age=age
        self.Cgpa=Cgpa
        self.uni=uni
# add objects
student1=student("maryam",35,3.8,"vu")
student2=student("minahil",45,4.0,"uet")
print("Student Name =",student1.name,"\nage =",student1.age,"\nCgpa =",student1.Cgpa,"\nuni =",student1.uni)
print("Student Name =",student2.name,"\nage =",student2.age,"\nCgpa =",student2.Cgpa,"\nuni =",student2.uni)