import React, { Component, Fragment } from 'react'

export class Header extends Component {
    render() {
        return (
            <Fragment>
                <header id="site-header">
                    <div class="container header-row">
                        <div class="header_block">
                            <a class="navbar-brand" href="/">
                                <img id="logo" src="media/whiteboard-logo.png" alt=""/>
                            </a>
                        </div>
                        <div class="header_block sbox">
                            <input type="text" placeholder="Search video..."/>
                        </div>
                    </div>
                </header>
            </Fragment>
            
        );
    }
}

export default Header


