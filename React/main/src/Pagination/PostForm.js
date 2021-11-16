import React from "react";

import axios from "axios";
import { useState } from "react";


// var express=require("express");
// var cors=require('cors');
// var app=express();
// app.use(cors());


function PostForm() {
    const url="http://127.0.0.1:5000/books"
    const [data,setdata] = useState({
        id:"",
        auther:"",
        title:"",
        language:"",
        data:""
    })

    

    function handle(e) {
        const newdata={...data}
        newdata[e.target.id]=e.target.value
        setdata(newdata)
        console.log(newdata)
    }

    function submit(e) {
        e.preventDefault();
        axios.post(url, {
            id:data.id,
            auther:data.auther,
            title:data.title,
            language:data.language,
            data:data.data
        },
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
    return(
        <div>
            <h3 className="container">Enter Book details</h3>
            <br/>
            <form onSubmit={(e)=>submit(e)}>

                <div class="container">
                    <div class=" bd-highlight mb-2">
                        <div class="input-group" >
                            <div className="container" >
                                <div className="row">
                                    <div className="col col-lg-2" >
                                        <span className="input-group-text" > 1.ID </span>
                                    </div>
                                    <div className="col-md-3 ">
                                        <input onChange={(e)=>handle(e)} id="id" value={data.id} placeholder="id" type="number" required></input>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div> 
                </div>


                <div class="container">
                    <div class=" bd-highlight mb-2">
                        <div class="input-group" >
                            <div className="container" >
                                <div className="row">
                                    <div className="col col-lg-2" >
                                        <span className="input-group-text" > 2.AUTHER </span>
                                    </div>
                                    <div className="col-md-3 ">
                                        <input onChange={(e)=>handle(e)} id="auther" value={data.auther} placeholder="auther" type="text" required></input>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div> 
                </div>
                    

                <div class="container">
                    <div class=" bd-highlight mb-2">
                        <div class="input-group" >
                            <div className="container" >
                                <div className="row">
                                    <div className="col col-lg-2" >
                                        <span className="input-group-text" > 3.TITLE </span>
                                    </div>
                                    <div className="col-md-3 ">
                                        <input onChange={(e)=>handle(e)} id="title" value={data.title} placeholder="title" type="text" required></input>
                                    </div>
                                </div>
                            </div> 
                        </div>
                    </div>
                </div>

                <div class="container">
                    <div class=" bd-highlight mb-3">
                        <div class="input-group" >
                            <div className="container" >
                                <div className="row">
                                    <div className="col col-lg-2" >
                                        <span className="input-group-text" > 4.LANGUAGE </span>
                                    </div>
                                    <div className="col-md-3 ">
                                        <input onChange={(e)=>handle(e)} id="language" value={data.language} placeholder="language" type="text" required></input>
                                    </div>
                                </div>
                            </div> 
                        </div>
                    </div>
                </div>
                {/* <input onChange={(e)=>handle(e)} id="auther" value={data.auther} placeholder="auther" type="text"></input> */}
                {/* <input onChange={(e)=>handle(e)} id="title" value={data.title} placeholder="title" type="text"></input> */}
                {/* <input onChange={(e)=>handle(e)} id="language" value={data.language} placeholder="language" type="text"></input> */}
                
                
                <div class="container">
                    <div class=" bd-highlight mb-3">
                        <div class="input-group" >
                            <div className="container" >
                                <div className="row">
                                    <div className="col col-lg-2" >
                                        <span className="input-group-text" > 5.UPLOAD </span>
                                    </div>
                                    <div className="col-md-3 ">
                                        <input onChange={(e)=>handle(e)} id="data" value={data.data} placeholder="image upload" type="file" required></input>
                                    </div>
                                </div>
                            </div> 
                        </div>
                    </div>
                </div>


                <div class="container">
                    <div class=" bd-highlight mb-3">
                        <div class="input-group" >
                            <div className="container" >
                                <div className="row">
                                    <div className="col col-lg-2" >
                                        <span className="input-group-text" > 5.Upload Video </span>
                                    </div>
                                    <div className="col-md-3 ">
                                        <input onChange={(e)=>handle(e)} id="data" value={data.data} placeholder="video upload" type="file" required></input>
                                    </div>
                                </div>
                            </div> 
                        </div>
                    </div>
                </div>
                
                
                <div class="container">
                    <div class="d-grid col-1">
                        <button class="btn btn-primary" type="submit">Submit</button>
                    </div>
                </div>

            </form>
        </div>
    );
}

export default PostForm;