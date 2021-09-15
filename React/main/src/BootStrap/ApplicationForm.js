import "../node_modules/bootstrap/dist/css/bootstrap.min.css"
import React, { useState } from "react";

 const ApplicationForm = () =>{

  return (
    <React.Fragment>
      <h1> <center>React-Bootstrap</center></h1>
      <hr/>

      <form>
        <div class=" bd-highlight mb-2">
          <center><button className = "btn btn-success">Application Form</button></center>
        </div>
        <div class="container">

          <div class=" bd-highlight mb-2">
            <div className="input-group">
              <div className="container">
                <div className="row">
                  <div className="col col-lg-2">
                    <span class="input-group-text">1.Username </span>
                  </div>
                
                  <div class="col col-lg-2">
                    <input
                      type="text" 
                      aria-label="First name" 
                      class="form-control"
                      placeholder="First name"
                      required
                    />
                  </div>

                  <div class="col col-lg-2">
                    <input
                      type="text" 
                      aria-label="First name" 
                      class="form-control"
                      placeholder="Middle name"
                    />
                  </div>
                  
                  <div class="col col-lg-2">
                    <input 
                      type="text" 
                      aria-label="Last name" 
                      class="form-control"
                      placeholder="Last name"
                      required
                    />
                  </div>
                  
                </div>
              </div>
            </div>
          </div>
          
          <div class=" bd-highlight mb-2">
            <div class="input-group" >
              <div className="container">
                <div className="row">
                  <div className="col col-lg-2">
                    <span className="input-group-text" >  2.Email  </span>
                  </div>
                  <div className="col col-md-6">
                    <input  type="email" aria-label="" class="form-control" placeholder="Enter email" required/>
                  </div>
                </div>
              </div>  
            </div>
          </div>
          
          <div class=" bd-highlight mb-2">
            <div class="input-group" >
              <div className="container">
                <div className="row">
                  <div className="col col-lg-2">
                    <span className="input-group-text" > 3.Password  </span>
                  </div>
                  <div className="col-md-6">
                      <input  type="password" aria-label="" class="form-control" placeholder="password" required/>
                  </div>
                </div>
              </div>  
            </div>
          </div>
          
          <div class=" bd-highlight mb-2">
            <div class="input-group" >
              <div className="container">
                <div className="row">
                  <div className="col col-lg-2">
                    <span className="input-group-text" > 4.Gender  </span>
                  </div>
                  <div className="col-md-6">
                    <div class="form-check form-check-inline">
                      <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1"/>
                      <label class="form-check-label" for="inlineRadio1">Male</label>
                    </div>
                    <div class="form-check form-check-inline">
                      <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="option2"/>
                      <label class="form-check-label" for="inlineRadio2">Female</label>
                    </div>
                    <div class="form-check form-check-inline">
                      <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio3" value="option3" />
                      <label class="form-check-label" for="inlineRadio3">  (Other)</label>
                    </div>
                  </div>
                </div>
              </div>  
            </div>
          </div>
          <div class=" bd-highlight mb-2">
            <div class="input-group" >
              <div className="container">
                  <div className="row" >
                    <div className="col col-lg-2">
                      <span className="input-group-text" > 5.Mobile  </span>
                    </div >
                    <div className="col-md-6" >
                        <input  type="tel" pattern="[0-9]{10}" class="form-control" placeholder="Phone number" required/>
                    </div>
                  </div>
                </div>
              </div>  
          </div>
          <div class=" bd-highlight mb-2">
            <div class="input-group" >
                <div className="container" >
                  <div className="row">
                    <div className="col col-lg-2" >
                      <span className="input-group-text" > 6.Address  </span>
                    </div>
                    <div className="col-md-6">
                      <input  type="text" aria-label="" class="form-control" placeholder="Enter Address" required/>
                    </div>
                  </div>
              </div> 
            </div>
          </div>
          
          <div className="container">
            <div className="row">
              <div class="col col-lg-5">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" value="" id="invalidCheck2" required />
                  <label class="form-check-label" for="invalidCheck2">
                    Agree to terms and conditions
                  </label>
                </div>
              </div>
            </div>
          </div>
              
          <div class=" bd-highlight mb-2">
            <div class="d-grid col-2 mx-auto">
              <button class="btn btn-primary" type="submit">Submit Form</button>
            </div>
          </div>


        </div>
      </form>

      
      

      {/* <ApplicationForm/> */}
    </React.Fragment>
  );
 };

export default ApplicationForm