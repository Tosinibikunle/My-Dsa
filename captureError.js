function captureErrorStack(errorObj, constructorOpt) {
  Error.captureStackTrace(errorObj, constructorOpt);
}

// Example (Node.js):
class CustomError {
  constructor(message) {
    this.message = message;
    captureErrorStack(this, CustomError);
  }
}
