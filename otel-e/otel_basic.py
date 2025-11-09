# otel_basic.py
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor


provider = TracerProvider()
trace.set_tracer_provider(provider)


console_exporter = ConsoleSpanExporter()
span_processor = SimpleSpanProcessor(console_exporter)
provider.add_span_processor(span_processor)


tracer = trace.get_tracer("demo.basic")

# 4) Crear spans 
with tracer.start_as_current_span("parent-span") as parent:
    parent.set_attribute("app.user_id", 123)
    parent.add_event("Parent span started")

    with tracer.start_as_current_span("child-span") as child:
        child.set_attribute("db.statement", "SELECT * FROM customers WHERE id=123")
        child.add_event("Query executed")

    parent.add_event("Parent span finishing")

print("All right")
