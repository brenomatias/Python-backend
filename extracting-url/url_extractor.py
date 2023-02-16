url = "bytebank.com/cambio?moedaOrigem=real"

text = 'abcd'
print(text[0:2])

url_base = url[0:19]
print(url_base)

url_parameter = url[20:]
print(url_parameter)

question_mark_index = url.find('?')

url_base2 = url[:question_mark_index]
url_parameter2 = url[question_mark_index+1:]

print(url_parameter2)

if url.find('!') == -1:
    print('the substring does not exist')
else:
    print(url.find('!'))

print('########################')

url2 = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
quest_mark_i = url2.find('?')
b_url = url2[:quest_mark_i]
print(b_url)
p_url = url2[quest_mark_i+1:]
print(p_url)

search_parameter = 'moedaOrigem'
index_parameter = p_url.find(search_parameter)
print(index_parameter)

index_value = index_parameter + len(search_parameter) + 1
print(index_value)
p_value = p_url[index_value:]
print(p_value)

print('####')
