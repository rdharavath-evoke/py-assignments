import React, {useState, useEffect} from "react";
import MaterialTable from 'material-table'
// import Link from 'material-table'

import { forwardRef } from 'react';

import AddBox from '@material-ui/icons/AddBox';
import ArrowUpward from '@material-ui/icons/ArrowUpward';
import Check from '@material-ui/icons/Check';
import ChevronLeft from '@material-ui/icons/ChevronLeft';
import ChevronRight from '@material-ui/icons/ChevronRight';
import Clear from '@material-ui/icons/Clear';
import DeleteOutline from '@material-ui/icons/DeleteOutline';
import Edit from '@material-ui/icons/Edit';
import FilterList from '@material-ui/icons/FilterList';
import FirstPage from '@material-ui/icons/FirstPage';
import LastPage from '@material-ui/icons/LastPage';
import Remove from '@material-ui/icons/Remove';
import SaveAlt from '@material-ui/icons/SaveAlt';
import Search from '@material-ui/icons/Search';
import ViewColumn from '@material-ui/icons/ViewColumn';
// import { Avatar, Grid } from "@material-ui/core";


function Materialtable() {

    const tableIcons = {
        Add: forwardRef((props, ref) => <AddBox {...props} ref={ref} />),
        Check: forwardRef((props, ref) => <Check {...props} ref={ref} />),
        Clear: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
        Delete: forwardRef((props, ref) => <DeleteOutline {...props} ref={ref} />),
        DetailPanel: forwardRef((props, ref) => <ChevronRight {...props} ref={ref} />),
        Edit: forwardRef((props, ref) => <Edit {...props} ref={ref} />),
        Export: forwardRef((props, ref) => <SaveAlt {...props} ref={ref} />),
        Filter: forwardRef((props, ref) => <FilterList {...props} ref={ref} />),
        FirstPage: forwardRef((props, ref) => <FirstPage {...props} ref={ref} />),
        LastPage: forwardRef((props, ref) => <LastPage {...props} ref={ref} />),
        NextPage: forwardRef((props, ref) => <ChevronRight {...props} ref={ref} />),
        PreviousPage: forwardRef((props, ref) => <ChevronLeft {...props} ref={ref} />),
        ResetSearch: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
        Search: forwardRef((props, ref) => <Search {...props} ref={ref} />),
        SortArrow: forwardRef((props, ref) => <ArrowUpward {...props} ref={ref} />),
        ThirdStateCheck: forwardRef((props, ref) => <Remove {...props} ref={ref} />),
        ViewColumn: forwardRef((props, ref) => <ViewColumn {...props} ref={ref} />)
        };




    const url="http://127.0.0.1:5000/books"
    const [data, setData] = useState([])
    useEffect(()=>{
        getBooks()
    },[])

    const getBooks=()=>{
        fetch(url).then(resp=>resp.json())
        .then(resp=>setData(resp))
    }


    const columns=[
        
        {field:'id',title:'ID',width:150, validate:rowData=>rowData.id===undefined?"Required":true},
        {field:'auther',title:'AUTHER',width:150, validate:rowData=>rowData.id===undefined?"Required":true},
        {field:"title",title:'TITLE',width:150,validate:rowData=>rowData.title===undefined?"Required":true},
        {field:"language",title:'LANGUAGE',width:150,validate:rowData=>rowData.language===undefined?"Required":true},
        { field:'img',title: 'Images',width:150,render:(rowData) =><img src={`http://127.0.0.1:5000/loadimage/${rowData.id}`} style={{width: 50, borderRadius: '60%'}}/> },
        { field:'mp4',title: 'Videos',width:150,render:(rowData) =>
                                                                    // <video  height="70px" controls="controls">
                                                                    //     <source src={`http://127.0.0.1:5000/loadvideo/${rowData.id}`}    
                                                                    //     type="video/mp4"/> 
                                                                    // </video>    }
                                                                    <video width="250" height="120" controls>
                                                                    <source src={`http://127.0.0.1:5000/loadvideo/${rowData.id}`} 
                                                                    type="video/mp4"/>
                                                                    
                                                                    </video> }

    ];


    return(
        <div style={{ height: 250, width: '100%' }} className="MaterialTable">
            <h1 align="center">React Table using API</h1>
            
            <MaterialTable
                title="Books Details"
                columns={columns}
                data={data}
                icons={tableIcons}
                options={{
                    actionsColumnIndex:-1, addRowPosition:"first",
                    paging:true,
                    pageSize:5,       // make initial page size
                    emptyRowsWhenPaging: false,   // To avoid of having empty rows
                    pageSizeOptions:[2,4,5,10,20]   // rows selection options

                  }}

                //   title={window.location.host.replace(/.stackblitz.io/, '') || 'Starter Template'}


                editable={{
                    onRowAdd:(newData)=>new Promise((resolve,reject)=>{
                        fetch(url,{
                            method:"POST",
                            headers:{
                                "Content-type":"application/json"
                            },
                            body:JSON.stringify(newData)
                        }).then(resp=>resp.json())
                        .then(resp=>{getBooks()
                            resolve()
                            })
                        }),
                        onRowUpdate:(newData,oldData)=>new Promise((resolve,reject)=>{
                            console.log(newData)
                            fetch(url+"/"+oldData.id,{
                                method:"PUT",
                                headers:{
                                    "Content-type":"application/json"
                                },
                                body:JSON.stringify(newData)
                            }).then(resp=>resp.json())
                            .then(resp=>{getBooks()
                                resolve()
                                })
                            }),
                        
                        onRowDelete:(oldData)=>new Promise((resolve,reject)=>{
                            fetch(url+"/"+oldData.id,{
                                method:"DELETE",
                                headers:{
                                    "Content-type":"application/json"
                                },
                                
                            }).then(resp=>console.log(resp))
                            .then(resp=>{getBooks()
                                resolve()
                                })
                            }),
                        
                    
                    }}


                


                
                // data={query =>
                //     new Promise((resolve, reject) => {
                //       let url = 'https://reqres.in/api/users?'
                //          url += 'per_page=' + query.pageSize
                //          url += '&page=' + (query.page + 1)
                //       fetch(url)
                //         .then(response => response.json())
                //         .then(result => {
                //           resolve({
                //               data: result.data,
                //               page: result.page - 1,
                //               totalCount: result.total,
                //           })
                //         })
                //     })
                //   }
                
            />
        </div>
    )
}

export default Materialtable;