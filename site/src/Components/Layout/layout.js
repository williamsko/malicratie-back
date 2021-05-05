import React from 'react';
import './layout.css';

export const Layout = (props) => (
    <div id="master_Container" className="container-fluid">
        {props.children}
    </div>
);