
import React, { useState } from "react";
// import { Redirect } from "react-router";
// import PaginationWithAPI from "./PaginationWithAPI";

const Addrow = () =>{
   
  // const [page, setpage] = useState(true)
  // if(page){
  //   return <Redirect to="/Addrow" />
  // }

  return (
    <React.Fragment>
      <h3> <center>Enter Book details</center></h3>
      <br/>
      <form>
        
        <div class="container">
          <div class=" bd-highlight mb-2">
            <div class="input-group" >
                <div className="container" >
                  <div className="row">
                    <div className="col col-lg-3" >
                      <span className="input-group-text" > 1.ID </span>
                    </div>
                    <div className="col-md-5">
                      <input  type="number" aria-label="" class="form-control" placeholder="Enter Id" required/>
                    </div>
                  </div>
              </div> 
            </div>
          </div>
          
          <div class=" bd-highlight mb-2">
            <div class="input-group" >
                <div className="container" >
                  <div className="row">
                    <div className="col col-lg-3" >
                      <span className="input-group-text" > 2.AUTHER </span>
                    </div>
                    <div className="col-md-5">
                      <input  type="text" aria-label="" class="form-control" placeholder="Enter Auther name" required/>
                    </div>
                  </div>
              </div> 
            </div>
          </div>
          
          <div class=" bd-highlight mb-2">
            <div class="input-group" >
                <div className="container" >
                  <div className="row">
                    <div className="col col-lg-3" >
                      <span className="input-group-text" > 3.TITLE </span>
                    </div>
                    <div className="col-md-5">
                      <input  type="text" aria-label="" class="form-control" placeholder="Enter title" required/>
                    </div>
                  </div>
              </div> 
            </div>
          </div>
          
          <div class=" bd-highlight mb-2">
            <div class="input-group" >
                <div className="container" >
                  <div className="row">
                    <div className="col col-lg-3" >
                      <span className="input-group-text" > 4.LANGUAGE </span>
                    </div>
                    <div className="col-md-5">
                      <input  type="text" aria-label="" class="form-control" placeholder="Enter language" required/>
                    </div>
                  </div>
              </div> 
            </div>
          </div>
          
          <div class=" bd-highlight mb-1">
            <div class="d-grid col-2 mx-auto">
              <button 
                class="btn btn-primary" 
                type="submit"
                // onClick={()=>setpage(true)}
                
                >Submit</button>
            </div>
          </div>


        </div>
      </form>

    </React.Fragment>
    
  );

};

export default Addrow