import xmlrpc.client
import streamlit as st
import matplotlib.pyplot as plt

stats_server = xmlrpc.client.ServerProxy("http://localhost:8072")

operation_types = stats_server.get_operation_types()

st.write(operation_types)

st.sidebar.header("Параметры")
st.sidebar.subheader('Период анализа')
start_date = st.sidebar.date_input('Начало периода')
end_date = st.sidebar.date_input('Конец периода')
interval = st.sidebar.slider('Интервал анализа данных, часы', 1, 4, 24)
# TODO или свободный ввод или из готовых
operation = st.sidebar.text_input('Тип операции', max_chars=20)


st.write("""
# Аналитика работы веб-сервиса
""")

# Валидация данных
# Период хотябы один день
params_valid = True

if params_valid:
    # TODO Получить из базы данные все логи за период
    logs = stats_server.get_in_period(1699199985, 1699499448)
    st.write(logs)
    # TODO Количетсово логов для каждого типа
    # гистограмму по количеству вызовов для типа операции (горизонтальной ось гистограммы – типы операций, вертикальная ось – количество вызовов).
    st.subheader("Количетство вызовов по типу операции")
    data = {'jack': 4098, 'sape': 4139}
    # st.bar_chart(data)

    # TODO Если есть тип то взять тольго его логи
    # TODO Разбить на каждые сутки и на каждый периоды
    # гистограмму по количеству вызова для типов операций на сутки (горизонтальная ось гистограммы – время 00:00-24:00 с заданными интервалом «slider» группировки, вертикальная ось – количество вызовов). Если тип операции «text_input» задан, то гистограмма строится для заданного типа операции, иначе – для всех.
    # if operation != "":
    #     st.subheader("Количество вызовов на сутки для типа операции '{}'".format(operation))
    # else:
    #     st.subheader("Количество вызовов на сутки для всех типов операций")

    # круговую диаграмму по количеству вызовов типа операции (размер сектора типа пропорционален количеству вызовов типа операции).

    labels = ["a", "b", "c", "d"]
    sizes = [15, 30, 45, 10]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)
    st.pyplot(fig)

    # TODO Длительности логов, взять среднее время для каждого типа
    # построить круговую диаграмму по времени вызовов типа операции (размер сектора типа пропорционален времени выполнения типа операции).