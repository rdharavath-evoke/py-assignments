import React from "react";

export default class Form extends React.Component{
    constructor(){
        super();
        this.state={
            name:"",
            salary:"",
            age:""
        }
    }

    submit()
    {
        let url="https://dummy.restapiexample.com/api/v1/create"
        let data=this.state;
        fetch(url,{
            method:'POST',
            headers:{
                'Content-Type': 'multipart/form-data'
            
            },
            body:JSON.stringify(data)
        }).then((result)=>{
            result.json().then((resp)=>{
                console.warn("resp",resp)
            })
        })
    }

    render(){
        return(
            <div>
                <h1>Simple Post ApI </h1>
                <input type="text" placeholder="name" value={this.state.name} name="name"
                onChange={(data)=>{this.setState({name:data.target.value})}}/> <br/>

                <input type="text" placeholder="salary" value={this.state.salary} name="salary"
                onChange={(data)=>{this.setState({salary:data.target.value})}}/> <br/>

                <input type="text" placeholder="age" value={this.state.age} name="age"
                onChange={(data)=>{this.setState({age:data.target.value})}}/> <br/>

                <button onClick={()=>{this.submit()}}> Submit</button>
            </div>
        )

    }


}