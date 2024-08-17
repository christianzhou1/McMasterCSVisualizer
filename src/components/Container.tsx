interface ContainerProps {
  as?: React.ElementType;
  children: React.ReactNode;
  className?: string;
}

export const Container = ({
  as: Element = "div",
  children,
  className,
  ...rest
}: ContainerProps) => {
  return (
    <Element
      {...rest}
      className={"px-5 w-full max-w-screen-md m-auto ${className}"}
    >
      {children}
    </Element>
  );
};
