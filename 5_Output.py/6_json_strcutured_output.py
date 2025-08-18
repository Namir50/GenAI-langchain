#we use json when we are using multiple languages in one project
#usually used when we need validation but dont need python objects
{
    'title':'student',
    'description': 'schema about the students',
    'type':'object',
    'properties':{
        'name':'string',
        'age':'integer'
    },
    'required':['name']
}