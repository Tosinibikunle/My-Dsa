function captureErrorStack(errorObj, constructorOpt) {
      Error.captureStackTrace(errorObj, constructorOpt);
      }

      // Example (Node.js):
      function CustomError(message) {
        this.message = message;
          captureErrorStack(this, CustomError);
          }
