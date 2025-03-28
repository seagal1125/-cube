import React, { useState } from 'react';

const [isWhiteFaceUp, setIsWhiteFaceUp] = useState(true);

const toggleFaces = () => {
  setIsWhiteFaceUp(!isWhiteFaceUp);
};

return (
  <div>
    <button 
      onClick={toggleFaces}
      className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
    >
      切换顺序
    </button>
    
    <div className="mt-4">
      {isWhiteFaceUp ? (
        <>
          <div className="white-face">白面</div>
          <div className="yellow-face">黄面</div>
        </>
      ) : (
        <>
          <div className="yellow-face">黄面</div>
          <div className="white-face">白面</div>
        </>
      )}
    </div>
  </div>
); 