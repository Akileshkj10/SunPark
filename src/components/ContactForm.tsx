"use client";

import { useState } from "react";
import type { FormField } from "@/content/types";
import { Button } from "./Button";

type ContactFormProps = {
  fields: FormField[];
};

export function ContactForm({ fields }: ContactFormProps) {
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [errors, setErrors] = useState<Record<string, string>>({});

  function validate(formData: FormData) {
    return fields.reduce<Record<string, string>>((nextErrors, field) => {
      const value = String(formData.get(field.name) ?? "").trim();

      if (field.required && !value) {
        nextErrors[field.name] = `${field.label} is required.`;
      }

      if (field.type === "email" && value && !value.includes("@")) {
        nextErrors[field.name] = "Enter a valid email address.";
      }

      return nextErrors;
    }, {});
  }

  return (
    <form
      className="contact-form"
      onSubmit={(event) => {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        const nextErrors = validate(formData);

        setErrors(nextErrors);
        setIsSubmitted(Object.keys(nextErrors).length === 0);
      }}
    >
      <div className="contact-form__grid">
        {fields.map((field) => {
          const error = errors[field.name];
          const errorId = `${field.name}-error`;

          return (
            <label
              className={
                field.type === "textarea"
                  ? "contact-form__field contact-form__field--wide"
                  : "contact-form__field"
              }
              key={field.name}
            >
              <span className="type-caption">
                {field.label}
                {field.required ? " *" : ""}
              </span>
              {field.type === "select" ? (
                <select
                  aria-describedby={error ? errorId : undefined}
                  aria-invalid={error ? "true" : "false"}
                  className="text-input"
                  defaultValue=""
                  name={field.name}
                >
                  <option disabled value="">
                    Select an option
                  </option>
                  {field.options?.map((option) => (
                    <option key={option} value={option}>
                      {option}
                    </option>
                  ))}
                </select>
              ) : field.type === "textarea" ? (
                <textarea
                  aria-describedby={error ? errorId : undefined}
                  aria-invalid={error ? "true" : "false"}
                  className="text-input text-input--textarea"
                  name={field.name}
                  rows={5}
                />
              ) : (
                <input
                  aria-describedby={error ? errorId : undefined}
                  aria-invalid={error ? "true" : "false"}
                  className="text-input"
                  name={field.name}
                  type={field.type}
                />
              )}
              {error ? (
                <span className="contact-form__error" id={errorId} role="alert">
                  {error}
                </span>
              ) : null}
            </label>
          );
        })}
      </div>

      <div className="contact-form__footer">
        <Button type="submit">Submit enquiry</Button>
        {isSubmitted ? (
          <p className="type-caption contact-form__status" role="status">
            Thank you. The enquiry form is validated and ready for submission
            routing once handling is approved.
          </p>
        ) : null}
      </div>
    </form>
  );
}
