import React from "react";
import axios from "axios";
import { useState } from "react";

function App() {
    const url="http://127.0.0.1:5000/employee"
    const [data,setdata] = useState({
        id:"",
        fname:"",
        lname:"",
        salary:"",
    })

    function handle(e) {
        const newdata={...data}
        newdata[e.target.id]=e.target.value
        setdata(newdata)
        console.log(newdata)
    }

    
    function employee(e) {
        e.preventDefault();
        axios.get(url,
        {
            headers:
            {
                'Content-Type': 'multipart/form-data',
                'Access-Control-Allow-Origin':'*'
            }
        })
        .then(res=>{
            console.log(res.data)
        })
    }

    // function notificasion(e) {
    //   return <h1>Employee with the id : {} created successfully</h1>;
    // }
    return(
        <div>
            <h3 className="container">get Employee details</h3>
            <br/>
            <form onSubmit={(e)=>employee(e)}>

              <element onChange={(e)=>handle(e)}/>


                {/* <input onChange={(e)=>handle(e)} id="id" value={data.id} placeholder="id" type="number"></input>
                <input onChange={(e)=>handle(e)} id="fname" value={data.fname} placeholder="fname" type="text"></input>
                <input onChange={(e)=>handle(e)} id="lname" value={data.lname} placeholder="lname" type="text"></input>
                <input onChange={(e)=>handle(e)} id="salary" value={data.salary} placeholder="salary" type="real"></input>  */}
                
                
                
                <div class="container">
                    <div class="d-grid col-1">
                        <button class="btn btn-primary" type="submit">employee</button>
                    </div>
                </div>

            </form>
            
        </div>
    );
}

export default App;































// import "./App.css";
// import { BrowserRouter as Router, Switch, Route, NavLink } from "react-router-dom";
// // import Addrow from "./Pagination/Addrow"
// // import PaginationWithAPI from "./Pagination/PaginationWithAPI"
// import Home from "./Pagination/Home"
// import PostForm from "./Pagination/PostForm"
// import Materialtable from "./Pagination/Materialtable";
// // import Form from "./Pagination/Form";


// function App() {

  
//     return (
//       <Router>
//         <div class="nav" >
//           <div class="d-inline p-2 bg-info text-white">
//             <NavLink to="/Home" >Home</NavLink>
//           </div>
//           <div class="d-inline p-2 bg-secondary text-white">
//             <NavLink to="/Add-book" class="link-dark">Add record</NavLink>
//           </div>
          
//           {/* <div class="d-inline p-2 bg-warning text-white">
//             <NavLink to="/result" class="link-success">total records</NavLink>
//           </div> */}
//           <div class="d-inline p-2 bg-warning text-white">
//             <NavLink to="/result" class="link-success">total records</NavLink>
//           </div>
//         </div>

//         <hr />
  
//         <Switch>
//           <Route exact path="/Home">
//             <Home />
//           </Route>
//           <Route path="/Add-book">
//             <PostForm />
//           </Route>
//           <Route path="/result">
//             {/* <PaginationWithAPI /> */}
//             {/* <Materialtable/> */}
//           </Route>
//         </Switch>
//       </Router>
//     );
//   }
  

// export default App;
































// import React from 'react';
// import notification from './Notification/notification'

// function App(){
//   const [intialData, setInitialData] = useState([{}])

//   useEffect(()=>{
//     fetch('/http://127.0.0.1:5000/employee',
//     {
//       headers : { 
//         'Content-Type': 'multipart/form-data',
//         'Accept': 'application/json'
//        }
//     }).then(
//       response=>response.json())
//     .then(data=>{console.log(data);
//       })
    
//   },[]);

//   return(
//     <div className="App">
//       <notification/>
//     </div>
//   )
// }

// export default App






// import React from "react";

// import axios from "axios";
// import { useState } from "react";


// function App() {
//     const url="http://127.0.0.1:5000/employee"
//      const [data,setdata] = useState({
//         id:"",
//         fname:"",
//         lname:"",
//         salary:""
//     })

    

//     // function handle(e) {
//     //     const newdata={...data}
//     //     newdata[e.target.id]=e.target.value
//     //     setdata(newdata)
//     //     console.log(newdata)
//     // }

//     function employee(e) {
//       const newdata={...data}
//       newdata[e.target.id]=e.target.value
//       setdata(newdata)
//       console.log(newdata)

//         e.preventDefault();
//         axios.post(url, {
//             id:data.id,
//             fname:data.fname,
//             lname:data.lname,
//             salary:data.salary,
//         },
//         {
//             headers:
//             {
//                 'Content-Type': 'multipart/form-data',
//                 'Access-Control-Allow-Origin':'*'
//             }
//         })
//         .then(res=>{
//             console.log(res.data)
//         })
//     }

//   return(
//     <div className="App">
//       {employee}
//       {/* {handle} */}
//     </div>
//   )
// }

// export default App








// import React from "react";

// export default class App extends React.Component{
//   state={
//     loading: true,
//     employee: null,
//   };

//   async componentDidMount(){
//     const url="http://127.0.0.1:5000/employee";
//     const response=await fetch(url);
//     const data = await response.json();
//     this.setState({person: data.results[0]})
//     console.log(data.results[0]);
//   }

//   render(){
//     return (
//       <div>
//         {this.state.loading ? <div>loading...</div> : <div>employee..</div>}
//       </div>
//     );
//   }
// }

















// import "./App.css";
// import { BrowserRouter as Router, Switch, Route, NavLink } from "react-router-dom";
// // import Addrow from "./Pagination/Addrow"
// // import PaginationWithAPI from "./Pagination/PaginationWithAPI"
// import Home from "./Pagination/Home"
// import PostForm from "./Pagination/PostForm"
// import Materialtable from "./Pagination/Materialtable";
// // import Form from "./Pagination/Form";


// function App() {

  
//     return (
//       <Router>
//         <div class="nav" >
//           <div class="d-inline p-2 bg-info text-white">
//             <NavLink to="/Home" >Home</NavLink>
//           </div>
//           <div class="d-inline p-2 bg-secondary text-white">
//             <NavLink to="/Add-book" class="link-dark">Add record</NavLink>
//           </div>
          
//           {/* <div class="d-inline p-2 bg-warning text-white">
//             <NavLink to="/result" class="link-success">total records</NavLink>
//           </div> */}
//           <div class="d-inline p-2 bg-warning text-white">
//             <NavLink to="/result" class="link-success">total records</NavLink>
//           </div>
//         </div>

//         <hr />
  
//         <Switch>
//           <Route exact path="/Home">
//             <Home />
//           </Route>
//           <Route path="/Add-book">
//             <PostForm />
//           </Route>
//           <Route path="/result">
//             {/* <PaginationWithAPI /> */}
//             <Materialtable/>
//           </Route>
//         </Switch>
//       </Router>
//     );
//   }
  

// export default App;















// import Expenses from './components/Expenses/Expenses';

// import NewExpense from './components/NewExpense/NewExpense';

// function App() {

//   const expenses = [
//     {
//       id: 'e1',
//       title: 'Honda',
//       amount: 54345.65,
//       date: new Date(2021,9,12),
//     },
//     {
//       id: 'e2',
//       title: 'Hero',
//       amount: 34459.43,
//       date: new Date(2020,2,16), 
//     },
//     {
//       id: 'e3',
//       title: 'Pulser',
//       amount: 5590.43,
//       date: new Date(2019,5,19), 
//     },
//     {
//       id: 'e4',
//       title: 'glammer',
//       amount: 62450.43,
//       date: new Date(2018,3,16), 
//     }
//   ]

//   return (
//     <div>
//       <NewExpense/>
//       <Expenses items={expenses} />
//     </div>
//   );
// }

// export default App;










