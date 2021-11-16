
























import "./App.css";
import { BrowserRouter as Router, Switch, Route, NavLink } from "react-router-dom";
// import Addrow from "./Pagination/Addrow"
// import PaginationWithAPI from "./Pagination/PaginationWithAPI"
import Home from "./Pagination/Home"
import PostForm from "./Pagination/PostForm"
import Materialtable from "./Pagination/Materialtable";
// import Form from "./Pagination/Form";


function App() {

  
    return (
      <Router>
        <div class="nav" >
          <div class="d-inline p-2 bg-info text-white">
            <NavLink to="/Home" >Home</NavLink>
          </div>
          <div class="d-inline p-2 bg-secondary text-white">
            <NavLink to="/Add-book" class="link-dark">Add record</NavLink>
          </div>
          
          {/* <div class="d-inline p-2 bg-warning text-white">
            <NavLink to="/result" class="link-success">total records</NavLink>
          </div> */}
          <div class="d-inline p-2 bg-warning text-white">
            <NavLink to="/result" class="link-success">total records</NavLink>
          </div>
        </div>

        <hr />
  
        <Switch>
          <Route exact path="/Home">
            <Home />
          </Route>
          <Route path="/Add-book">
            <PostForm />
          </Route>
          <Route path="/result">
            {/* <PaginationWithAPI /> */}
            <Materialtable/>
          </Route>
        </Switch>
      </Router>
    );
  }
  

export default App;















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










