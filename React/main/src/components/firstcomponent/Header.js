
const Header =({title})=>{
    return(
        <div>
            <h1 style={{color:"red"}}>Hello react</h1>
        </div>
    )
}

Header.defaultProps={
    title:"Welcome to react"
}

Header.prototypes={
    title: PropTypes
}

export default Header