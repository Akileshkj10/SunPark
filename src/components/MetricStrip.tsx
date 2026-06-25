import type { Metric } from "@/content/types";

type MetricStripProps = {
  metrics: Metric[];
};

export function MetricStrip({ metrics }: MetricStripProps) {
  return (
    <div className="metric-strip">
      {metrics.map((metric) => (
        <article className="metric-card" key={`${metric.value}-${metric.label}`}>
          <p className="type-display-md metric-card__value">{metric.value}</p>
          <h3 className="type-label-md">{metric.label}</h3>
          <p>{metric.context}</p>
        </article>
      ))}
    </div>
  );
}
