# Extracting Table Names from Query

def get_tables(query):
    
    query_tokens = query.split()
    
#     indexes = []
    
#     for i in range(len(query_tokens)):
        
#         if query_tokens[i] == 'FROM':
            
#             indexes.append(i)
        
    indexes1 = [i for i in range(len(query_tokens)) if query_tokens[i] == 'FROM']
    
    indexes2 = [i for i in range(len(query_tokens)) if query_tokens[i] == 'JOIN']
    
    indexes_final = indexes1 + indexes2
    
#     table_list = []
    
#     for j in indexes:
        
#         if (query_tokens[j+1] not in ['SELECT', '(']) & (query_tokens[j-1] not in ['DAY', 'MONTH', 'YEAR']):
            
#             table_list = query_tokens[j+1].replace("\"", "")
    
    table_list1 = [query_tokens[j+1].replace("\"", "") for j in indexes1 if (query_tokens[j+1] not in ['SELECT', '(', '(SELECT']) & (query_tokens[j-1] not in ['DAY', 'MONTH', 'YEAR'])]
    
    table_list2 = [query_tokens[j+1].replace("\"", "") for j in indexes2 if (query_tokens[j+1] not in ['SELECT', '(', '(SELECT']) & (query_tokens[j-1] not in ['DAY', 'MONTH', 'YEAR'])]
    
    table_list = table_list1 + table_list2
            
    return table_list
