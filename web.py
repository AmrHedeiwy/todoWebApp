import streamlit as st
import func

todos = func.get_todo()

def add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    todos.append(new_todo)
    func.write_todo(todos)

st.title('My Todo App')
st.subheader('This is m todo app.')
st.write('This app is to increase your productivity.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todo(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder='Add a new todo...',
              on_change=add_todo, key='new_todo')