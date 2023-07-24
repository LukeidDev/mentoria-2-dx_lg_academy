import pandas as pd

class EmployerData:

    def __init__ (self, path_file):
        self.path_file = path_file
        self.dados = pd.read_excel(path_file)

    def funcionarios_por_cargo(self):
        return self.dados.groupby('Job Title').size()
    
    def funcionarios_por_cor_pele(self):
        return self.dados.groupby('Ethnicity').size()
    
    def funcionarios_por_genero(self):
        return self.dados.groupby('Gender').size()
    
    def funcionarios_por_cargo_grupo(self):
        return self.dados.groupby('Job Title').apply(lambda x: x[['Full Name', 'Age', 'Gender', 'Ethnicity']].to_dict('records'))

