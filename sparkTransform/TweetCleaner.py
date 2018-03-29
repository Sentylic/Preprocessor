from pyspark import keyword_only
from pyspark.ml.pipeline import Transformer 
from pyspark.ml.param.shared import HasInputCol, HasOutputCol
import re
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

class TweetCleaner(Transformer, HasInputCol, HasOutputCol): 
    @keyword_only 
    def __init__(self, inputCol=None, outputCol=None): 
        super(TweetCleaner, self).__init__() 
        kwargs = self._input_kwargs
        self.setParams(**kwargs) 
    @keyword_only 
    def setParams(self, inputCol=None, outputCol=None): 
        kwargs = self._input_kwargs 
        return self._set(**kwargs) 
    def _transform(self, dataset): 
        out_col = self.getOutputCol() 
        in_col = dataset[self.getInputCol()] 
        def f(s):
            import re
            text = s
            text = re.sub(r'http\S+', '', text)
            text = re.sub(r'\&\S+;', '', text)
            text = re.sub(r'\\u[0-9]+', '', text)
            text = re.sub(r'@\S+', '', text)
            text = re.sub(r'#', '',text)
            return text.strip()  
        t = StringType() 
        return dataset.withColumn(out_col, udf(f, t)(in_col)) 