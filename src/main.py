import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

options = PipelineOptions()
p = beam.Pipeline(options=options)

with beam.Pipeline as pipeline:
    pass

line = pipeline | 'ReadMyFile' >> beam.io.ReadFromText('/Users/Anurag/PycharmProjects/ApacheBeam/data/input/input_data.txt')

