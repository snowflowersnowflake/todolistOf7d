const addButton = document.getElementById('add');
const inputElement = document.getElementById('content');
const todoListDom = document.getElementById('todoList');
const todos = JSON.parse(localStorage.getItem('todos')) || [];

// 新增方法
function addItem(content) {
  let todoItem = document.createElement('li');
  todoItem.innerText = content;
  document.getElementById('todoList').appendChild(todoItem);

  // 保存到本地
  todos.push(content);
  localStorage.setItem('todos', JSON.stringify(todos));
}

// 删除方法
function deleteItem(element) {
  element.remove();
  // 保存到本地
  todos.map((value, index) => {
    if(value === element.innerText.trim()) {
      todos.splice(index, 1);
    }
  })
  localStorage.setItem('todos', JSON.stringify(todos));
}

// 点击添加按钮
addButton.addEventListener('click', () => {
  if(inputElement.value) {
    addItem(inputElement.value.trim());
  }
})

// 点击条目删除
todoList.addEventListener('click', (event) => {
  if(event.target.tagName === 'LI') {
    deleteItem(event.target);
  }
}, true)

// 默认读取localstorage
todos.forEach(content => {
  let todoItem = document.createElement('li');
  todoItem.innerText = content;
  todoListDom.appendChild(todoItem);
});