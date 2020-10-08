
import  requests
from bs4 import BeautifulSoup
import pandas as pd
import dataframe_image as dfi

def parseData():
    ## Initial data
    url = 'https://www.curs.md/ro/curs_valutar_banci'
    response = requests.get(url)
    parse_html = BeautifulSoup(response.text, 'html.parser')
    ##

    ## --- > Bank name
    clas_bank_name = parse_html.find(id="tabelBankValute").select('a')

    bank_list = []
    for elem in clas_bank_name:
        s2 = elem.get_text()
        bank_list.append(s2)

    bank_list_new = [x.replace('\n', '') for x in bank_list]
    bank_list_new = [x.replace(' ', '') for x in bank_list_new]
    bank_list_name =[]
    count = 0
    for number in bank_list_new:
        count+=1
        bank_list_name.append(number)
        #print(str(count)+ str(' ') +number)


    #USD Vinzare / Cumparare

    data_USD = parse_html.body.findChildren(class_='column-USD column-ind-0')
    set_of_data_USD = []
    for resul in data_USD:

        usd_text = resul.get_text()
        set_of_data_USD.append(usd_text)
    del set_of_data_USD[0]



    usd_cumparare = set_of_data_USD[::2]
    usd_vinzare = []

    for i in range(len(usd_cumparare)): #перебираем элементы списка (в пределах длины первого списка)
        if set_of_data_USD[i] == usd_cumparare[i]: #сравниваем элементы первого списка с элементами второго списка
            del set_of_data_USD[i] #добавляем в пустой список элемент из первого, если он меньше
            usd_vinzare.append(set_of_data_USD[i])

    del usd_cumparare[0]
    del usd_vinzare[0]

    ### end

    # Eur vinzare / cumparare




    data_EUR = parse_html.body.findChildren(class_='column-EUR column-ind-1')
    set_of_data_EUR = []
    for resul in data_EUR:

        eur_text = resul.get_text()
        set_of_data_EUR.append(eur_text)
    del set_of_data_EUR[0]



    eur_cumparare = set_of_data_EUR[::2]
    eur_vinzare = []

    for i in range(len(eur_cumparare)): #перебираем элементы списка (в пределах длины первого списка)
        if set_of_data_EUR[i] == eur_cumparare[i]: #сравниваем элементы первого списка с элементами второго списка
            del set_of_data_EUR[i] #добавляем в пустой список элемент из первого, если он меньше
            eur_vinzare.append(set_of_data_EUR[i])

    del eur_cumparare[0]
    del eur_vinzare[0]




    ## End



    #Rub vinzare/cumparare

    data_RUB = parse_html.body.findChildren(class_='column-RUB column-ind-2')
    set_of_data_RUB = []
    for resul in data_RUB:

        rub_text = resul.get_text()
        set_of_data_RUB.append(rub_text)
    del set_of_data_RUB[0]



    rub_cumparare = set_of_data_RUB[::2]
    rub_vinzare = []

    for i in range(len(rub_cumparare)): #перебираем элементы списка (в пределах длины первого списка)
        if set_of_data_RUB[i] == rub_cumparare[i]: #сравниваем элементы первого списка с элементами второго списка
            del set_of_data_RUB[i] #добавляем в пустой список элемент из первого, если он меньше
            rub_vinzare.append(set_of_data_RUB[i])

    del rub_cumparare[0]
    del rub_vinzare[0]




    ## end


    ## RON vinzare / cumparare

    #Rub vinzare/cumparare

    data_RON = parse_html.body.findChildren(class_='column-RON column-ind-3')
    set_of_data_RON = []
    for resul in data_RON:

        ron_text = resul.get_text()
        set_of_data_RON.append(ron_text)
    del set_of_data_RON[0]



    ron_cumparare = set_of_data_RON[::2]
    ron_vinzare = []

    for i in range(len(ron_cumparare)): #перебираем элементы списка (в пределах длины первого списка)
        if set_of_data_RON[i] == ron_cumparare[i]: #сравниваем элементы первого списка с элементами второго списка
            del set_of_data_RON[i] #добавляем в пустой список элемент из первого, если он меньше
            ron_vinzare.append(set_of_data_RON[i])

    del ron_cumparare[0]
    del ron_vinzare[0]




    ## end
    desired_width=320

    pd.set_option('display.width', desired_width)

    pd.set_option('display.max_columns',10)


    table1 = (list(zip(bank_list_name,usd_cumparare,usd_vinzare,eur_cumparare,eur_vinzare, rub_cumparare, rub_vinzare,ron_cumparare,ron_vinzare)))


    df = pd.DataFrame(table1,columns=['Denumirea Bancii',
                                      'Cumparare USD',  'Vinzare USD',
                                      'Cumparare EUR',  'Vinzare EUR',
                                      'Cumparare RUB',  'Vinzare RUB',
                                      'Cumparare RON',  'Vinzare RON',])

    return df


vallet_data = parseData()



dfi.export(vallet_data, 'data.png')
