import React from 'react';

import './Header.css';
import logo from 'assets/logo.svg';

class Header extends React.Component {
    render() {
        return (
            <header className="header">
              <img src={logo} className="header-logo" alt="logo" />
              <h1 className="header-title">Welcome</h1>
            </header>
        );
    }
}

export default Header;
