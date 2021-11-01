import React, { useState } from 'react';

const ApplicationForm = () => {
    const [values, setValues] = useState({
        firstname:"",
        lastname:"",
        email:"",
    });

    const [submitted, setSubmitted]=useState(false);
    const [valid,setValid]=useState(false);

    const firstnamehandler = (event) =>{
        setValues({...values, firstname: event.target.value})
    }
    const lastnamehandler = (event) =>{
        setValues({...values, lastname: event.target.value})
    }
    const emailhandler = (event) =>{
        setValues({...values, email: event.target.value})
    }

    const handlesubmit = (event) => {
        event.preventDefault();
        if (values.firstname && values.lastname && values.email){
            setValid(true)
        }
        setSubmitted(true)
    }



    
    return (
        <div className="container">
            <form className="register-form" onSubmit={handlesubmit}>
                {submitted && valid ? <div className="success-message"> success! Thank you for Register </div> :null}
                <input 
                    onChange={firstnamehandler}
                    value={values.firstname}
                    className='form-feild'
                    type="text" 
                    placeholder='first name'

                />
                {submitted && !values.firstname?<span>please enter firstname</span>:null}
                <br/>
                <input 
                    onChange={lastnamehandler}
                    value={values.lastname}
                    type="text" 
                    placeholder='last name'
                />
                {submitted && !values.lastname?<span>please enter lastname</span>:null}
                <br/>
                <input 
                    onChange={emailhandler}
                    value={values.email}
                    type="text" 
                    placeholder='email'
                    
                />
                {submitted && !values.email? <span>please enter email</span>:null}
                <br/>
                <button
                    type='submit'
                    className='form-feild'
                    placeholder='Register'
                    
                />
            </form>
        </div>
        
    );
}

export default ApplicationForm