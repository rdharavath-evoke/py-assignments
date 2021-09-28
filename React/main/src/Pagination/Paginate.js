import React from 'react';
import { DataGrid,GridToolbarExport,GridToolbarContainer} from '@material-ui/data-grid';
// import { Pagination } from 'evergreen-ui';
import 'bootstrap/dist/css/bootstrap.min.css';
import { PaginationItem, PaginationLink } from "reactstrap"
import Pagination from 'react-bootstrap/Pagination';


    const columns=[
        {field:'id',headerName:'ID',width:150, },
        {field:'name',headerName:'NAME',width:150},
        {field:'age',headerName:'AGE',width:150},
        {field:"profession",headerName:'PROFESSION',width:170},
        {field:"address",headerName:'ADDRESS',width:150},
    ];

    // const headerName = {
    //   textAlign: "center",
    //   color: "Red",
    //   fontSize: "22px"
    //  }


    const rows = [
        { id: 1, name: 'Arun', age: 12, profession:'Student',address:'Warangal'},
        { id: 2, name: 'Varun', age: 43, profession:'Teacher',address:'Hyderabad'},
        { id: 3, name: 'Pranav', age: 41, profession:'Megician',address:'Kakinada' },
        { id: 4, name: 'Varun bharav', age: 34, profession:'Actor',address:'Bejawada' },
        { id: 5, name: 'Manas', age: 73, profession:'Professior',address:'Karnool' },
        { id: 6, name: 'Dinesh', age: 61, profession:'Lecturer',address:'Nelloor' },
        { id: 7, name: 'Ramu', age: 72, profession:'Scientist',address:'Hyderabad' },
        { id: 8, name: 'Varun Babu', age: 24, profession:'Engineer',address:'Hyderabad' },
        { id: 9, name: 'Charan', age: 48, profession:'Technician',address:'Hyderabad' },
        { id: 10, name: 'Eshwar', age: 32, profession:'Mechanical',address:'Vishakapatnam' },
        { id: 11, name: 'Fani', age: 40, profession:'Doctor',address:'Hyderabad' },
        { id: 12, name: 'Ganesh', age: 49, profession:'Driver',address:'Warangal' },
        { id: 13, name: 'Hemanth', age: 38, profession:'Collector',address:'Guntur' },
        { id: 14, name: 'Ivar', age: 73, profession:'Police',address:'Kodada' },
        { id: 15, name: 'Jagan', age: 51, profession:'Actor',address:'Khammam' },
        { id: 16, name: 'Karan', age: 32, profession:'Teacher',address:'Tirupathi' },
        { id: 17, name: 'Lala', age: 64, profession:'Teacher',address:'Hyderabad' },
        { id: 18, name: 'Nani', age: 58, profession:'Sports',address:'Vizag' },
        { id: 19, name: 'Sahith', age: 64, profession:'Coach',address:'Warangal' },
        { id: 20, name: 'Tharun', age: 58, profession:'Teacher',address:'Hyderabad' },
      ];


function MyExportButton() {
    return (
      <GridToolbarContainer>
        <GridToolbarExport />
      </GridToolbarContainer>
    );
  }
    
  export default function Paginate() {
    const [pageSize, setPageSize] = React.useState(5);
    
    return (
      <div style={{ height: 350, width: '80%' }}>
        <h4 style={{color:'green'}}>
         How to use export data as CSV in ReactJS?
        </h4>
        <DataGrid rows={rows} columns={columns} 
          pageSize={pageSize} 
          onPageSizeChange={(newPageSize) => setPageSize(newPageSize)}
          rowsPerPageOptions={[1, 2, 3, 4, 5]}
          components={{
            Toolbar: MyExportButton,
          }}
          filterModel={{
            items: [
              { Field: 'name',
                operator: 'ends with', 
                value: 'v' },
            ],
          }}
          
          
  
        />
        <div className="custom-style">
          
          <center class="centered">
            <Pagination>
              <Pagination.Prev />
              <Pagination.Ellipsis />
              <Pagination.Item>{3}</Pagination.Item>
              <Pagination.Item>{4}</Pagination.Item>
              <Pagination.Item>{5}</Pagination.Item>
              <Pagination.Ellipsis />
              <Pagination.Next />
            </Pagination> 

            <Pagination>
              <h4 style={{color:'brown'}}>Reference :: </h4><br/> 
              <PaginationItem>
                  <PaginationLink href="https://www.tutorialspoint.com">tutorialspoint</PaginationLink>
              </PaginationItem>
              <PaginationItem>
                  <PaginationLink href="https://www.google.com">google</PaginationLink>
              </PaginationItem>
              <PaginationItem>
                  <PaginationLink href="https://www.reactjs.com">reactjs</PaginationLink>
              </PaginationItem>
              <PaginationItem>
                  <PaginationLink href="https://www.bootstrap.com">Bootstrap</PaginationLink>
                </PaginationItem>
              <PaginationItem>
                <PaginationLink href="https://www.python.com">python</PaginationLink>
              </PaginationItem>
            </Pagination>
 
            <Pagination>
              
            </Pagination> 


          </center>
        </div>
        
      </div>
    );
  }















