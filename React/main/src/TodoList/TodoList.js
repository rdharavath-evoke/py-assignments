import React from "react";

const TodoList = ({todolist, deleteHandler}) =>{
    return(
        <div>
            {todolist.map((todo,index) => 
            <div key={index}>
                <h5>{todo} &nbsp; <button onClick={()=>deleteHandler(index)}>Delete</button></h5>
            </div>)}
        </div>
    );
}

export default TodoList;


// import React, {useState} from 'react';
// import TodoList from './TodoList';


// const App =()=>{
//     const [task, setTask] = useState("");
//     const [todos, setTodos] = useState([])

//     const changeHandler = e => {
//         setTask(e.target.value)
//     }

//     const submitHandler = e =>{
//         e.preventDefault();
//         const newTodos = [...todos,task];
//         setTodos(newTodos);
//         setTask("");
//     }
//     const deleteHandler = (indexValue)=>{
//         const newtodos = todos.filter((todo,index)=>index!==indexValue)
//         setTodos(newtodos)
//     }

//     return(
//         <div>
//             <center>
//                 <div className="card">
//                     <div className="cord-body">
//                         <h2 className="card-title">Todo Management Application</h2> 
//                         <form onSubmit={submitHandler}>
//                             <input size="30" type="text" name="task" value={task} onChange={changeHandler} /> &nbsp;
//                             <input type="submit" value="add" name="add" />

//                         </form>
//                         <TodoList todolist={todos} deleteHandler={deleteHandler}/>
//                     </div>
//                 </div>
//             </center>
//         </div>
//     );
// }

// export default App;
