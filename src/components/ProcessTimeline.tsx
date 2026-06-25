import type { ProcessStep } from "@/content/types";

type ProcessTimelineProps = {
  steps: ProcessStep[];
};

export function ProcessTimeline({ steps }: ProcessTimelineProps) {
  return (
    <ol className="process-timeline">
      {steps.map((step, index) => (
        <li className="process-timeline__item" key={step.title}>
          <span className="process-timeline__index">
            {String(index + 1).padStart(2, "0")}
          </span>
          <div>
            <h3 className="type-title-sm">{step.title}</h3>
            <p>{step.body}</p>
          </div>
        </li>
      ))}
    </ol>
  );
}
