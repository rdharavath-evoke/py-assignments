import { useState } from 'react';
import ExpenseDate from './ExpenseDate';
import './ExpenseItem.css';
function ExpenseItem(props)
{
    const [title, setTitle] = useState(props.title)

    const ClickHandler = () =>{
        setTitle('Updated!');
        console.log(title);
    };
    return (
    <div className="expense-item">
        <ExpenseDate date={props.date}/>
        <div className="expense-item__description">
            <h2>{props.title}</h2>
            <div className="expense-item__price">${props.amount}</div>
            <div>onclick={ClickHandler}</div>
        </div>
    </div>);
}

export default ExpenseItem                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                