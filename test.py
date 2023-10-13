
# # counter = 1

# # def generate_client_id(counter):
# #     # Format the counter with leading zeros and concatenate with "C"
# #     client_id = f'C{counter:02d}'

# #     return client_id

# # print(generate_client_id(counter))
# # counter += 1
# # print(generate_client_id(counter))
# # counter += 1
# # print(generate_client_id(counter))
# # counter += 1
# # print(generate_client_id(counter))
# # counter += 1

# # CREATE TABLE client (
# #     client_id VARCHAR(30) PRIMARY KEY,
# #     f_name VARCHAR(255),
# #     m_name VARCHAR(255),
# #     l_name VARCHAR(255),
# #     phone_no VARCHAR(15),
# #     email VARCHAR(255),
# #     pwd VARCHAR(255),
# #     role VARCHAR(50)
# # );




# global counter , lis
# counter = 1
# lis = []

# def generate_client_id():
#     # global counter
#     # Format the counter with leading zeros and concatenate with "C"
#     if lis == []:
#         counter = 1
        
#     else:
#         counter = lis[-1]
#         counter = counter[1:]
#         counter = int(counter) + 1
#         # client_id = 'C' + str(counter).zfill(3)

#     client_id = 'C' + str(counter).zfill(3)
#     lis.append(client_id)
#     print(lis)
#     return client_id

# Client_id = generate_client_id()
# print(Client_id)
# Client_id = generate_client_id()
# print(Client_id)
# Client_id = generate_client_id()
# print(Client_id)
# Client_id = generate_client_id()
# print(Client_id)
# # print(Client_id)
# # print(Client_id)
# # print(Client_id)
# # print(Client_id)
# # print(Client_id)
# # print(Client_id)
