import React from "react";

function Footer() {
    return (
        <footer className="bg-dark text-light py-3">
            <div className="container">
                <div className="row align-items-center text-center text-md-start">
                    {/* Left Section */}
                    <div className="col-md-5 mb-3 mb-md-0">
                        <p className="mb-0">
                            2024{" "}
                            
                                Blog
                            | All Rights reserved
                        </p>
                    </div>

                    {/* Center Section */}
                    <div className="col-md-4 mb-3 mb-md-0 text-center text-md-start">
                    <p className="mb-0">
                        </p>
                    </div>
                    
                    {/* Right Section */}
                    <div className="col-md-3">
                        <ul className="list-unstyled d-flex justify-content-center justify-content-md-end mb-0">
                            <li className="ms-3">
                                <a 
                                    href="https://facebook.com/desphixs" 
                                    className="text-light fs-5" 
                                    target="_blank" 
                                    rel="noopener noreferrer"
                                >
                                    <i className="fab fa-github-square" />
                                </a>
                            </li>
                            <li className="ms-3">
                                <a 
                                    href="https://twitter.com/desphixs" 
                                    className="text-light fs-5" 
                                    target="_blank" 
                                    rel="noopener noreferrer"
                                >
                                    <i className="fab fa-linkedin" />
                                </a>
                            </li>
                           
                        </ul>
                    </div>
                </div>
            </div>
        </footer>
    );
}

export default Footer;
