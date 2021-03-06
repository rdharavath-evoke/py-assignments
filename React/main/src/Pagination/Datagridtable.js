import React from 'react';
import { DataGrid,GridToolbarExport,GridToolbarContainer} from '@material-ui/data-grid';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useEffect, useState } from "react";
import axios from 'axios';
import { Link } from 'react-router-dom'




    const columns=[
        {field:'id',headerName:'ID',width:150 },
        {field:'auther',headerName:'AUTHER',width:150,editable: true},
        {field:"title",headerName:'TITLE',width:150,editable: true},
        {field:"language",headerName:'LANGUAGE',width:150,editable: true},
        {headerName:"Actions",field:"updel", width:150, cellRendererFramework:(params)=><div>
          <Link class="btn btn-primary">View</Link>
          <Link class="btn btn-outline-primary">Update</Link>
          <Link class="btn btn-outline-primary">Delete</Link>
          
        </div>}
    ];


function MyExportButton() {
    return (
      <GridToolbarContainer>
        <GridToolbarExport />
      </GridToolbarContainer>
    );
  }
    
  export default function PaginationWithAPI() {
    const [pageSize, setPageSize] = React.useState(5);

    


    const [book,setbook]=useState([])
  // const [search,setsearch]=useState("")

  const getbookData = async () =>{
    try{
      const data=await axios.get("http://127.0.0.1:5000/books");
      console.log(data.data);
      setbook(data.data)
      
    }
    catch(e){
        console.log(e);
      }
  }
  useEffect(()=>{
    getbookData();
  }, []);




    
    return (
      <div style={{ height: 350, width: '80%' }}>
        <h4 style={{color:'green'}}> Pagination Table </h4>
        <DataGrid 
          rows={book} 
          columns={columns} 
          pageSize={pageSize} 
          onPageSizeChange={(newPageSize) => setPageSize(newPageSize)}
          rowsPerPageOptions={[1, 2, 3, 4, 5, 10, 15]}
          components={{Toolbar: MyExportButton,}}


        />
      </div>
    );
  }















