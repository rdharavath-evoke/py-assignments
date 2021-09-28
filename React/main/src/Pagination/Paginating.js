import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

const Paginate =()=> {

    return(
        <nav aria-label="Page navigation example">
        <ul class="pagination justify-content">
            <ul class="pagination">
                <li class="page-item"><a class="page-link" href="#">Previous</a></li>
                <li class="page-item"><a class="page-link" href="#">1</a></li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
                <li class="page-item"><a class="page-link" href="#">Next</a></li>
            </ul>
        </ul>
        

        <h3 style={{color: 'blue'}}>working with icons</h3>
        <ul class="pagination">
            <li class="page-item">
                <a class="page-link" href="#" aria-label="">
                <span aria-hidden="true">&laquo;</span>
                <span class="sr-only">Previous</span>
                </a>
            </li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item">
                <a class="page-link" href="#" aria-label="">
                <span aria-hidden="true">&raquo;</span>
                <span class="sr-only">Next</span>
                </a>
            </li>
        </ul>
         
        <h3 style={{color: 'blue'}}>Disbled and active state</h3>
        <ul class="pagination">
            <li class="page-item disabled">
            <a class="page-link" href="#" tabindex="-1">Previous</a>
            </li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item active">
            <a class="page-link" href="#">2 <span class="sr-only"></span></a>
            </li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item">
            <a class="page-link" href="#">Next</a>
            </li>
        </ul>



        </nav>
    );
}

export default Paginate;