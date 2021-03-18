import React, {Component} from 'react';

import CustomersService from './CustomersService'


const customersService = new CustomersService();


class  CustomersList  extends  Component {

    constructor(props) {
        super(props);
        this.state  = {
            products: [],
        };
        this.nextPage  =  this.nextPage.bind(this);
        this.handleDelete  =  this.handleDelete.bind(this);
    }
    componentDidMount() {
        var  self  =  this;
        customersService.getCustomers().then(function (result) {
            console.log(result);
            self.setState({ products:  result.data})
        });
    }
    handleDelete(e,pk){
        var  self  =  this;
        customersService.deleteCustomer({pk :  pk}).then(()=>{
            var  newArr  =  self.state.customers.filter(function(obj) {
                return  obj.pk  !==  pk;
            });
    
            self.setState({products:  newArr})
        });
    }
    
    nextPage(){
        var  self  =  this;
        console.log(this.state.nextPageURL);
        customersService.getCustomersByURL(this.state.nextPageURL).then((result) => {
            self.setState({ products:  result.data})
        });
    }
    render() {
    
        return (
            <div  className="customers--list">
                {this.state.products.map( c =>
                <div>{c.name}</div>  )}
                <div>Hello</div>
            </div>
        );
    }
}
export  default  CustomersList;