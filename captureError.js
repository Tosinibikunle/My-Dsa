function captureErrorStack(errorObj, constructorOpt) {
  
  Error.captureStackTrace(errorObj, constructorOpt);
}

class CustomError {
  
  constructor(message) {
    
    this.message = message;
    captureErrorStack(this, CustomError);
  }
}
